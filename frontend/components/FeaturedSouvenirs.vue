<template>
	<section class="bg-gray-50 py-12">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="text-center">
				<h2 class="text-primary-600 text-base font-semibold tracking-wide uppercase">精選推薦</h2>
				<p class="mt-1 text-3xl font-extrabold text-gray-900 sm:text-4xl sm:tracking-tight">
					特色股票紀念品
				</p>
				<p class="mx-auto mt-5 max-w-xl text-lg text-gray-500">
					精選台灣上市公司發行的最具特色紀念品，從限量公仔到精美文創，讓您的收藏更加豐富。
				</p>
			</div>

			<div class="mt-12">
				<div class="grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-3 xl:gap-x-8">
					<SouvenirCard
						v-for="souvenir in featuredSouvenirs"
						:key="souvenir.id"
						:souvenir="souvenir"
					/>
				</div>
			</div>

			<div class="mt-12 text-center">
				<NuxtLink
					to="/featured"
					class="btn-primary inline-flex items-center px-6 py-3"
				>
					<span>查看更多精選紀念品</span>
					<svg
						class="-mr-1 ml-2 h-5 w-5"
						xmlns="http://www.w3.org/2000/svg"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M17 8l4 4m0 0l-4 4m4-4H3"
						/>
					</svg>
				</NuxtLink>
			</div>
		</div>
	</section>
</template>

<script setup>
	// Sample data - in a real app, this would come from an API or store
	const featuredSouvenirs = [
		{
			id: 1,
			name: '台積電 40週年紀念金幣',
			companyName: '台積電',
			companyId: 1,
			category: '紀念幣章',
			description:
				'為慶祝台積電成立40週年而特別發行的純金紀念幣，正面刻有創辦人張忠謀肖像，背面為台積電晶圓廠剪影。限量發行1000枚，每枚附贈證書及精美收藏盒。',
			imageUrl:
				'https://images.pexels.com/photos/8957028/pexels-photo-8957028.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
			releaseYear: 2022,
			status: '限量',
			rating: 4.9,
			reviewCount: 128,
			isLimited: true,
		},
		{
			id: 2,
			name: '鴻海科技日限定機器人模型',
			companyName: '鴻海',
			companyId: 2,
			category: '公仔模型',
			description:
				'鴻海科技日限定版機器人模型，高約30公分，採用高品質材料製作，擁有多個可動關節。模型細節精緻，完美呈現鴻海在機器人技術上的創新成就。',
			imageUrl:
				'https://images.pexels.com/photos/8566245/pexels-photo-8566245.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
			releaseYear: 2023,
			status: '熱門',
			rating: 4.7,
			reviewCount: 89,
			isLimited: true,
		},
		{
			id: 3,
			name: '華碩ROG電競限定手錶',
			companyName: '華碩',
			companyId: 3,
			category: '電子產品',
			description:
				'華碩ROG品牌限定款智能手錶，採用高解析度AMOLED螢幕，內置多種電競主題錶面及功能，支援健康監測與通知提醒，為電競玩家設計的完美配件。',
			imageUrl:
				'https://images.pexels.com/photos/437037/pexels-photo-437037.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
			releaseYear: 2024,
			status: '新上架',
			rating: 4.8,
			reviewCount: 42,
			isLimited: false,
		},
	];
</script>
